variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "eu-west-1"
}

variable "app_name" {
  description = "Elastic Beanstalk application name"
  type        = string
  default     = "devops-flask-app"
}

variable "environment_name" {
  description = "Elastic Beanstalk environment name"
  type        = string
  default     = "devops-flask-env"
}

variable "instance_type" {
  description = "EC2 instance type for EB environment"
  type        = string
  default     = "t2.micro"
}
