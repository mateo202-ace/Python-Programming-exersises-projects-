from fabric import Connection

# Define the remote server details
REMOTE_HOST = "192.168.1.100"  # Replace with the actual server IP
REMOTE_USER = "admin"          # Replace with the actual username
REMOTE_PASSWORD = "password"   # Replace with the actual password

# Define the task: Deploy a web application
def deploy_web_app():
    """
    Automates the deployment of a web application on a remote server.
    """
    try:
        # Establish a connection to the remote server
        conn = Connection(
            host=REMOTE_HOST,
            user=REMOTE_USER,
            connect_kwargs={"password": REMOTE_PASSWORD}
        )

        # Update the package list and install updates
        print("Updating system packages...")
        conn.sudo("apt update && apt upgrade -y")

        # Install necessary dependencies
        print("Installing dependencies...")
        conn.sudo("apt install -y python3 python3-pip nginx git")

        # Clone the web application repository
        print("Cloning the web application repository...")
        conn.run("git clone https://github.com/example/web-app.git /var/www/web-app")

        # Install Python dependencies
        print("Installing Python dependencies...")
        conn.run("pip3 install -r /var/www/web-app/requirements.txt")

        # Configure Nginx
        print("Configuring Nginx...")
        nginx_config = """
        server {
            listen 80;
            server_name example.com;

            location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            }
        }
        """
        conn.run("echo '{}' > /etc/nginx/sites-available/web-app".format(nginx_config))
        conn.sudo("ln -s /etc/nginx/sites-available/web-app /etc/nginx/sites-enabled")
        conn.sudo("nginx -t && systemctl restart nginx")

        # Start the web application
        print("Starting the web application...")
        conn.run("nohup python3 /var/www/web-app/app.py &")

        print("Deployment completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    deploy_web_app()