import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inventory Managment CLI")

    parser.add_argument("inventory", help="Inventory Command")
    parser.add_argument(
        "-a", "--add", required=False, nargs="*", help="Adds item to inventory"
    )
    parser.add_argument(
        "-s",
        "--show",
        action="store_true",
        required=False,
        help="Shows the inventory available",
    )

    args = parser.parse_args()

    if args.add:
        with open("inventory.txt", "a+") as f:
            for item in args.add:
                # f.write(f"{item}\n")
                print(f"{item} was added to inventory")

    if args.show:
        with open("inventory.txt", "r") as f:
            print("AVAILABLE INVENTORY")
            print("--------------------\n")
            print(f.read())

    print("args ->", args)
