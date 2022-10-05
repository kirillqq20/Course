output "resource_group_name" {
  value = azurerm_resource_group.kir-terraform.name
}

output "azurerm_windows_virtual_machine" {
  value = azurerm_windows_virtual_machine.kir-terraform.source_image_reference
}

output "public_ip" {
  value = azurerm_public_ip.kir-terraform-ip.id
}

