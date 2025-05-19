resource "azurerm_resource_group" "rg" {
  name     = "gary_test_${var.environment}"
  location = var.location
  tags     = merge(var.tags, {
    Environment = var.environment
  })
}
