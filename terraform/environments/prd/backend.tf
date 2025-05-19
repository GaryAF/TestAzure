terraform {
  backend "azurerm" {
    resource_group_name  = "rg-prd-demo"
    storage_account_name = "stoprddemo"
    container_name       = "terraform-state-prd"
    key                  = "terraform.tfstate"
  }
} 