
terraform {
  backend "azurerm" {
    resource_group_name  = "rg-rec-demo"
    storage_account_name = "storecdemo"
    container_name       = "terraform-state-rec"
    key                  = "terraform.tfstate"
  }
}