terraform {
  backend "s3" {
    bucket   = "cq55609-bread"
    key      = "terraform/terraform.tfstate"
    region   = "ru-1"
    endpoint = "s3.timeweb.com"

    skip_region_validation      = true
    skip_credentials_validation = true
  }
}
