variable "resource_group_location" {
  default     = "westeurope"
  description = "Location of the resource group"
}

variable "resource_group_name" {
  default     = "kir-serv-test-terraform"
  description = "Resourse group name"
}

variable "firerwall_ip" {
  default = "3.120.117.202"
  description = "azurerm_mysql_firewall_rule"  
}
