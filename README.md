# � Bigo Live Agency Commission Calculator

A comprehensive Streamlit application for calculating host commissions and bean conversions for Bigo Live agencies.

## Features

- **Host Commission Calculator**: Calculate commissions with diamond conversion
- **Agent Bean Calculator**: Simple bean calculations for agents
- **Excel Export**: Download results as Excel files
- **Responsive Design**: Works on mobile and desktop
- **Cloud Ready**: Configured for AWS and Cloudflare deployment

## Local Development

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TacitBlade/Bigo-LIve-Agency-Commision-Calculator.git
   cd Bigo-LIve-Agency-Commision-Calculator
   ```

2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Cloud Deployment

### AWS Deployment Options

#### Option 1: AWS Elastic Beanstalk
1. Install AWS CLI and EB CLI
2. Initialize Elastic Beanstalk:
   ```bash
   eb init -p python-3.11 bigo-commission-calculator
   eb create production
   eb deploy
   ```

#### Option 2: AWS ECS with Docker
1. Build Docker image:
   ```bash
   docker build -t bigo-calculator .
   ```
2. Push to ECR and deploy via ECS

#### Option 3: AWS Lambda (Serverless)
Use AWS Lambda with API Gateway for serverless deployment.

### Cloudflare Pages Deployment

1. Connect your GitHub repository to Cloudflare Pages
2. Set build settings:
   - **Framework preset**: None
   - **Build command**: `pip install -r requirements.txt`
   - **Build output directory**: Leave empty
   - **Root directory**: Leave empty

3. Add environment variables:
   - `PYTHON_VERSION`: `3.11`
   - `PORT`: `8501`

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t bigo-calculator .
   ```

2. Run the container:
   ```bash
   docker run -p 8501:8501 bigo-calculator
   ```

### Environment Variables

The following environment variables can be configured:

- `PORT`: Application port (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: 0.0.0.0)
- `STREAMLIT_SERVER_PORT`: Server port (uses PORT if set)

## Configuration Files

- `.streamlit/config.toml`: Streamlit configuration
- `Dockerfile`: Container configuration
- `Procfile`: Process configuration for platforms like Heroku
- `runtime.txt`: Python version specification
- `.ebextensions/`: AWS Elastic Beanstalk configuration

## Usage

1. **Select Calculator Mode**: Choose between Host Commission Calculator or Agent Bean Calculator
2. **Enter Data**: Input host/agent names and beans earned
3. **Calculate**: Click the calculate button to process results
4. **Export**: Download results as Excel files
5. **Review**: Check the summary and breakdown information

## Support

For support and questions, please open an issue on GitHub.

---
© 2025 Alpha Agency & T Star Agency. All rights reserved.
