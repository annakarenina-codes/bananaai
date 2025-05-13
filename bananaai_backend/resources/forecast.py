from flask import request
from flask_restful import Resource
from bananaai_backend.extensions import db
from bananaai_backend.models import Forecast, Product, InventoryMovement
from datetime import datetime, timedelta
import numpy as np

class ForecastListResource(Resource):
    def get(self):
        forecasts = Forecast.query.all()
        return [
            {
                'id': forecast.id,
                'product_id': forecast.product_id,
                'date': forecast.date.isoformat(),
                'predicted_demand': forecast.predicted_demand,
                'historical_demand': forecast.historical_demand,
                'forecast_error': forecast.forecast_error,
                'confidence_interval_lower': forecast.confidence_interval_lower,
                'confidence_interval_upper': forecast.confidence_interval_upper
            } for forecast in forecasts
        ]
    
    def post(self):
        data = request.get_json()
        
        product_id = data.get('product_id')
        
        # Validate the product exists
        product = Product.query.get_or_404(product_id)
        
        # Get historical sales data for the product (last 30 days)
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=30)
        
        movements = InventoryMovement.query.filter(
            InventoryMovement.product_id == product_id,
            InventoryMovement.movement_type == 'sell',
            InventoryMovement.movement_date >= start_date,
            InventoryMovement.movement_date <= end_date
        ).all()
        
        # Calculate historical demand (simple sum of sales)
        historical_demand = sum(movement.quantity for movement in movements)
        
        # Simple moving average forecast (very basic)
        # In a real application, you would use more sophisticated methods
        predicted_demand = historical_demand / 30  # average daily demand
        
        # Set confidence interval (simple implementation)
        forecast_error = 0.1  # 10% error assumption
        confidence_interval_lower = predicted_demand * (1 - forecast_error)
        confidence_interval_upper = predicted_demand * (1 + forecast_error)
        
        # Create forecast for next 7 days
        forecasts = []
        for i in range(1, 8):
            forecast_date = datetime.utcnow().date() + timedelta(days=i)
            
            new_forecast = Forecast(
                product_id=product_id,
                date=forecast_date,
                predicted_demand=round(predicted_demand),
                historical_demand=round(historical_demand / 30),  # daily average
                forecast_error=forecast_error,
                confidence_interval_lower=round(confidence_interval_lower),
                confidence_interval_upper=round(confidence_interval_upper)
            )
            
            db.session.add(new_forecast)
            forecasts.append(new_forecast)
        
        db.session.commit()
        
        return {
            'message': 'Forecasts generated successfully',
            'forecast_count': len(forecasts)
        }, 201
    
    def delete(self):
        try:
            # Delete all forecasts
                deleted_count = Forecast.query.delete()
                db.session.commit()

                if deleted_count > 0:
                    return {"message": f"{deleted_count} forecasts deleted successfully"}, 200
                else:
                    return {"message": "No forecasts to delete"}, 204
        except Exception as e:
                db.session.rollback()  # In case of any error, rollback the transaction
                return {"message": f"Error deleting forecasts: {str(e)}"}, 500

class ForecastResource(Resource):
    def get(self, forecast_id):
        forecast = Forecast.query.get_or_404(forecast_id)
        
        return {
            'id': forecast.id,
            'product_id': forecast.product_id,
            'date': forecast.date.isoformat(),
            'predicted_demand': forecast.predicted_demand,
            'historical_demand': forecast.historical_demand,
            'forecast_error': forecast.forecast_error,
            'confidence_interval_lower': forecast.confidence_interval_lower,
            'confidence_interval_upper': forecast.confidence_interval_upper
        }
    def put(self, forecast_id):
        forecast = Forecast.query.get_or_404(forecast_id)
        data = request.get_json()

        # Update only the fields that are provided
        forecast.predicted_demand = data.get('predicted_demand', forecast.predicted_demand)
        forecast.forecast_error = data.get('forecast_error', forecast.forecast_error)
        forecast.confidence_interval_lower = data.get('confidence_interval_lower', forecast.confidence_interval_lower)
        forecast.confidence_interval_upper = data.get('confidence_interval_upper', forecast.confidence_interval_upper)

        db.session.commit()

        return {
            'message': 'Forecast updated successfully',
            'forecast': {
                'id': forecast.id,
                'product_id': forecast.product_id,
                'date': forecast.date.isoformat(),
                'predicted_demand': forecast.predicted_demand,
                'historical_demand': forecast.historical_demand,
                'forecast_error': forecast.forecast_error,
                'confidence_interval_lower': forecast.confidence_interval_lower,
                'confidence_interval_upper': forecast.confidence_interval_upper
            }
        }, 200
    
    def delete(self, forecast_id):
        forecast = Forecast.query.get_or_404(forecast_id)
        db.session.delete(forecast)
        db.session.commit()
        
        return {"message": f"Forecast with ID {forecast_id} deleted successfully"}, 200


class ProductForecastResource(Resource):
    def get(self, product_id):
        # Get forecasts for a specific product
        forecasts = Forecast.query.filter_by(product_id=product_id).all()
        
        return [
            {
                'id': forecast.id,
                'date': forecast.date.isoformat(),
                'predicted_demand': forecast.predicted_demand,
                'historical_demand': forecast.historical_demand,
                'confidence_interval_lower': forecast.confidence_interval_lower,
                'confidence_interval_upper': forecast.confidence_interval_upper
            } for forecast in forecasts
        ]