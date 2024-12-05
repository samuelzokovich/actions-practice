# Required providers
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

# Provider configuration
provider "azurerm" {
  features {}
}

# Variables (Optional)
variable "resource_group_name" {
  description  = "The name of the Resource Group"
  type      = string
  default  = "my-resource-group"
}

variable "location" {
  description = "The location/region for the Resource Group"
  type      = string
  default   = "East US"
}

# Resource: Azure Resource Group
resource "azurerm_resource_group" "rg" {
  name   = var.resource_group_name
  location = var.location
}

# Outputs
output "resource_group_name" {
  description = "The name of the created Resource Group"
  value  = azurerm_resource_group.rg.name
}

output "resource_group_location" {
  description = "The location of the created Resource Group"
  value  = azurerm_resource_group.rg.location
}

