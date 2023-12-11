variable "project" {
    description = "Your GCP Project ID"
    default     = "taxilytics"
    type        = string
}

variable "bucket" {
    description = "Your GCP bucket name"
    default     = "taxilytics_data_lake"
    type        = string
}

variable "region" {
    description = "Region for GCP resources"
    default     = "us-east5"
    type        = string
}

variable "storage_class" {
    description = "Storage class type for your bucket"
    default = "STANDARD"
    type        = string
}

variable "stg_bq_dataset" {
    description = "BigQuery dataset for raw data"
    default     = "staging"
    type        = string
}

variable "prod_bq_dataset" {
    description = "BigQuery dataset for upstream data visualization"
    default     = "prod"
    type        = string
}