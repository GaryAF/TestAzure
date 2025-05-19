terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
}

terraform {
  backend "azurerm" {
    resource_group_name  = "rg-gc-azer-tf"
    storage_account_name = "gencloudazuretf"
    container_name       = "terraform-state"
    key                  = "terraform.tfstate"
  }
}
