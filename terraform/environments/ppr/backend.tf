terraform {
  backend "azurerm" {
    resource_group_name  = "rg-ppr-demo"
    storage_account_name = "stopprdemo"
    container_name       = "terraform-state-ppr"
    key                  = "terraform.tfstate"
  }
} 