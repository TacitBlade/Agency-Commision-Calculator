# 🚀 Deployment Guide

This guide covers deployment options for the Bigo Live Agency Commission Calculator to AWS and Cloudflare.

## Quick Start (Local Development)

### Windows
```batch
setup.bat
run.bat
```

### Linux/Mac
```bash
chmod +x setup.sh run.sh
./setup.sh
./run.sh
```

## ☁️ Cloud Deployment Options

### 1. Streamlit Cloud (Recommended for Quick Deploy)

1. **Push to GitHub**: Ensure your code is in a GitHub repository
2. **Visit**: https://share.streamlit.io/
3. **Connect**: Your GitHub repository
4. **Deploy**: Select `streamlit_app.py` as the main file

### 2. AWS Deployment

#### Option A: AWS Elastic Beanstalk

1. **Install AWS CLI and EB CLI**:
   ```bash
   pip install awsebcli
   ```

2. **Initialize and Deploy**:
   ```bash
   eb init -p python-3.11 bigo-commission-calculator
   eb create production
   eb deploy
   ```

3. **Configuration**: Uses `.ebextensions/streamlit.config`

#### Option B: AWS ECS with Docker

1. **Build Docker Image**:
   ```bash
   docker build -t bigo-calculator .
   ```

2. **Push to ECR**:
   ```bash
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ECR_URI
   docker tag bigo-calculator:latest YOUR_ECR_URI/bigo-calculator:latest
   docker push YOUR_ECR_URI/bigo-calculator:latest
   ```

3. **Deploy via ECS**: Create ECS service using the pushed image

#### Option C: AWS Lambda (Serverless)

Use AWS Lambda with API Gateway for serverless deployment. Requires additional configuration for Streamlit.

### 3. Cloudflare Pages

#### Method 1: GitHub Integration (Recommended)

1. **Connect Repository**:
   - Go to Cloudflare Pages dashboard
   - Connect your GitHub repository

2. **Build Settings**:
   - **Framework preset**: None
   - **Build command**: `pip install -r requirements.txt && streamlit run streamlit_app.py --server.port=8080 --server.address=0.0.0.0 &`
   - **Build output directory**: Leave empty
   - **Root directory**: Leave empty

3. **Environment Variables**:
   ```
   PYTHON_VERSION=3.11
   PORT=8080
   STREAMLIT_SERVER_ADDRESS=0.0.0.0
   ```

#### Method 2: Direct Upload

1. **Build Locally**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Upload**: Drag and drop your project folder to Cloudflare Pages

### 4. Docker Deployment (Any Cloud Provider)

#### Build Image
```bash
docker build -t bigo-calculator .
```

#### Run Locally
```bash
docker run -p 8501:8501 bigo-calculator
```

#### Deploy to Cloud
- **Google Cloud Run**: `gcloud run deploy`
- **Azure Container Instances**: `az container create`
- **DigitalOcean App Platform**: Use Docker deployment option

### 5. Heroku Deployment

1. **Install Heroku CLI**
2. **Create App**:
   ```bash
   heroku create bigo-commission-calculator
   ```
3. **Deploy**:
   ```bash
   git push heroku main
   ```

Uses `Procfile` for process configuration.

## 🔧 Configuration Files

| File | Purpose |
|------|---------|
| `streamlit_app.py` | Main application |
| `requirements.txt` | Python dependencies |
| `.streamlit/config.toml` | Streamlit configuration |
| `Dockerfile` | Container configuration |
| `Procfile` | Process configuration (Heroku) |
| `runtime.txt` | Python version specification |
| `.ebextensions/` | AWS Elastic Beanstalk config |
| `_pages.toml` | Cloudflare Pages config |

## 🌍 Environment Variables

Set these environment variables in your deployment platform:

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 8501 | Application port |
| `STREAMLIT_SERVER_ADDRESS` | 0.0.0.0 | Server bind address |
| `STREAMLIT_SERVER_PORT` | Uses PORT | Streamlit server port |

## 🔍 Troubleshooting

### Common Issues

1. **Port Issues**: Ensure your cloud provider's port matches the PORT environment variable
2. **Dependencies**: All dependencies must be in `requirements.txt`
3. **File Paths**: Use relative paths for cross-platform compatibility
4. **Memory Limits**: Some free tiers have memory restrictions

### Platform-Specific Notes

#### AWS Elastic Beanstalk
- Uses `.ebextensions/streamlit.config`
- Requires proper WSGI configuration
- May need custom container commands

#### Cloudflare Pages
- Limited to static sites, may need Workers for dynamic content
- Consider using Streamlit Cloud instead

#### Docker
- Exposes port 8501 by default
- Includes health check endpoint
- Optimized for production use

## 📊 Monitoring & Scaling

### Health Checks
The application includes a health check endpoint at `/_stcore/health`.

### Scaling
- **Horizontal**: Deploy multiple instances behind a load balancer
- **Vertical**: Increase memory/CPU resources

### Monitoring
- **Logs**: Check application logs for errors
- **Metrics**: Monitor CPU, memory, and response times
- **Uptime**: Set up uptime monitoring

## 🔐 Security Considerations

1. **HTTPS**: Always use HTTPS in production
2. **Environment Variables**: Store sensitive data in environment variables
3. **CORS**: Configure CORS settings appropriately
4. **Rate Limiting**: Implement rate limiting for public deployments

## 💡 Tips for Success

1. **Test Locally**: Always test your changes locally first
2. **Small Deployments**: Deploy frequently with small changes
3. **Monitoring**: Set up logging and monitoring from day one
4. **Backup**: Keep backups of your data and configurations
5. **Documentation**: Document your deployment process

## 🆘 Support

If you encounter issues:

1. Check the deployment logs
2. Verify all environment variables are set
3. Ensure all files are included in your deployment
4. Test the Docker image locally if using containers
5. Check the platform-specific documentation

For additional help, create an issue in the GitHub repository.
