FROM python:3.10-slim-buster  
  
# Set environment variables to ensure that Python output is sent straight to the terminal  
ENV PYTHONUNBUFFERED=1  
  
# Working directory in the container  
WORKDIR /home  
  
# Copy root app_server inside services folder  
COPY /services/app_server /home/services/app_server
  
# Install the dependencies for each service  
RUN pip install --no-cache-dir\
 -r /home/services/app_server/requirements.txt
  
# Expose the port the app runs on  
EXPOSE 8080

# Command to run the application  
CMD ["uvicorn", "services.app_server.app_server.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "2"]
