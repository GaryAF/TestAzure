locals {
  environment = "ppr"
}

module "main" {
  source = "../"
  environment = local.environment
}