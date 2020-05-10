import discord


def get_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = get_token()


def get_client_id():
    with open("clientid.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
client_id = get_client_id()


def main():
    client = discord.Client()
    client.run(token)


if __name__ == "__main__":
    main()