variable "environment" {
  description = "Environnement de déploiement (rec, ppr, prd)"
  type        = string
}

variable "location" {
  description = "Région Azure où déployer les ressources"
  type        = string
  default     = "northeurope"
}