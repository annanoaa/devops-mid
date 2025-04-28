terraform {
  required_version = ">= 0.12"
}

# Create local directories for deployment
resource "local_file" "directories" {
  for_each = toset([
    "deploy/blue",
    "deploy/green",
    "logs"
  ])
  
  content     = ""
  filename    = "${path.module}/${each.key}/.gitkeep"
  
  provisioner "local-exec" {
    command = "mkdir -p ${path.module}/${each.key}"
  }
}

# Create a local variable to track which environment is active
resource "local_file" "active_env" {
  content  = "blue"
  filename = "${path.module}/deploy/active_env.txt"
}

# Output information about created resources
output "deployment_directories" {
  value = [for dir in local_file.directories : dir.filename]
}

output "active_environment" {
  value = local_file.active_env.content
} 