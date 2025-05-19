variable "resource_group_name" {
  description = "Nom du groupe de ressources"
  type        = string
}

variable "environment" {
  description = "Environnement de déploiement (development, preprod, production)"
  type        = string
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
    ManagedBy = "Terraform"
    Project   = "Azure Terraform"
  }
}
