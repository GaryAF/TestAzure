locals {
  environment_names = {
    rec = "Recette"
    ppr = "Pré-production"
    prd = "Production"
  }
}

resource "azurerm_resource_group" "rg" {
  name     = "gary_test${var.environment}"
  location = var.location
}