variable "project" {
    description = "Your GCP Project ID"
    default     = "taxilytics"
    type        = string
}

variable "region" {
    description = "Region for GCP resources"
    default     = "us-east5"
    type        = string
}

variable "stg_bq_dataset" {
    description = "BigQuery dataset for raw data"
    default     = "stg"
    type        = string
}

variable "prod_bq_dataset" {
    description = "BigQuery dataset for transformed data"
    default     = "prod"
    type        = string
}