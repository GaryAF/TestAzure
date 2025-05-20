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

resource "azurerm_container_registry" "acr" {

  name                = "garytestacr_${var.environment}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Basic"
  admin_enabled       = true
}