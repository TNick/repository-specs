# Containerized Deployment

Use this building block when the repository owns container images or a Compose
orchestrated deployment.

## Required

- Keep Dockerfiles and Compose files under clearly named deployment folders.
- Pin base images and install dependencies from committed lockfiles.
- Pass runtime configuration through environment or mounted configuration,
  never by baking secrets into images.
- Provide safe start, stop, logs, shell, rebuild, and smoke-test commands.
- Ensure stop operations preserve persistent data by default.
