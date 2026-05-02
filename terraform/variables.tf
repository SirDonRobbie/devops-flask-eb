variable "aws_region" {
  description = "AWS region used for deployment"
  type        = string
  default     = "us-east-1"
}

variable "application_name" {
  description = "Elastic Beanstalk application name"
  type        = string
  default     = "devops-flask-eb-app-v2"
}

variable "environment_name" {
  description = "Elastic Beanstalk environment name"
  type        = string
  default     = "devops-flask-eb-env-v2"
}


