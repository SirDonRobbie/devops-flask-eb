variable "aws_region" {
  description = "AWS region used for deployment"
  type        = string
  default     = "us-east-1"
}

variable "application_name" {
  description = "Elastic Beanstalk application name"
  type        = string
  default     = "devops-flask-eb-app"
}

variable "environment_name" {
  description = "Elastic Beanstalk environment name"
  type        = string
  default     = "devops-flask-eb-env"
}

variable "solution_stack_name" {
  description = "Elastic Beanstalk Python platform"
  type        = string
  default     = "64bit Amazon Linux 2023 v4.3.0 running Python 3.11"
}


