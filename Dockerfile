# 🔴 Outdated base image (known CVEs)
FROM node:12

# 🔴 Running as root (default behavior)
WORKDIR /app

# 🔴 Installing packages without cleanup (security + size issue)
RUN apt-get update && apt-get install -y curl vim

# 🔴 Copy everything (could include secrets)
COPY . .

# 🔴 Expose app port
EXPOSE 3000

# 🔴 Start app
CMD ["node", "app.js"]