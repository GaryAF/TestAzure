locals {
  environment = "rec"
}

module "main" {
  source = "../"
  environment = local.environment
}