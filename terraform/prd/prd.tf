locals {
  environment = "prd"
}

module "main" {
  source = "../"
  environment = local.environment
}