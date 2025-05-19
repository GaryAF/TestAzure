locals {
  environment_names = {
    rec = "Recette"
    ppr = "Pré-production"
    prd = "Production"
  }
}

resource "azurerm_resource_group" "rg" {
  name     = "gary_test_good_${var.environment}"
  location = var.location
}