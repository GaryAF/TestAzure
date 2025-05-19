variable "resource_group_name" {
  description = "Nom du groupe de ressources"
  type        = string
  default     = "rg-test-github"
}

variable "location" {
  description = "Région Azure où le groupe de ressources sera créé"
  type        = string
  default     = "francecentral"
}

variable "tags" {
  description = "Tags à appliquer au groupe de ressources"
  type        = map(string)
  default = {
    Environment = "Production"
    Project     = "Azure Terraform"
  }
}
