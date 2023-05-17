variable "swarm-manager-host" {
  type        = string
  sensitive   = true
  description = "Address of swarm manager"
}

variable "app-name" {
  type        = string
  description = "Name of app"
}

variable "app-version" {
  type        = string
  description = "Version of Docker image of app"
  default     = "1.0"
}

variable "app-host" {
  type        = string
  description = "Hostname of app"
}

variable "app-dotenv-b64" {
  type        = string
  description = "Base64 encoded .env file"
  sensitive   = true
}

variable "cpu-limit" {
  type        = number
  description = "CPU limit in nanoseconds"
  default     = 100 * 10000000
}

variable "memory-limit" {
  type        = number
  description = "Memory limit in bytes"
  default     = 128 * 1024 * 1024
}
