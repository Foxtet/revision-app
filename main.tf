resource "google_cloud_run_v2_service" "app" {
  name = "revision-app"
  location = var.region
  template {
    containers {
      image = var.image
      ports { container_port = 8080 }
    }
  }
}
