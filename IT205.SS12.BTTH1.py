cart_items = [
    {
     	"id": "P001", 
     	"name": "Dien thoai iPhone 15",
     	"number": 1,
     	"price": 25000000
    },
    {
     	"id": "P002",
     	"name": "Op lung Silicon", 
     	"number": 2, 
     	"price": 150000
    }
]

is_run_true = True

while is_run_true:
    print("+================================================+")
    print("|         SHOPEE CART MANAGEMENT SYSTEM          |")
    print("+================================================+")
    print("| 1. Xem chi tiêt giỏ hàng & Tính tổng tiên      |")
    print("| 2. Thêm sản phẩm mới / Cộng dôn sô lượng       |")
    print("| 3. Cập nhật sô lượng của một sản phẩm          |")
    print("| 4. Xóa sản phẩm khỏi giỏ hàng                  |")
    print("| 5. Thoát chương trình                          |")
    print("+================================================+")

    choice = input("Mời bạn chọn chức năng (1-5): ").strip()

    match choice:

        case "1":

            print("\n--- Chi tiết giỏ hàng ---")

            index_header = "STT"
            product_id_header = "Mã SP"
            product_name_header = "Tên sản phâm"
            quantity_header = "Số lượng"
            price_header = "Đơn giá"
            total_header = "Thành tiền"

            max_index_length = len(index_header)
            max_product_id_length = len(product_id_header)
            max_product_name_length = len(product_name_header)
            max_quantity_length = len(quantity_header)
            max_price_length = len(price_header)
            max_total_length = len(total_header)

            index = 1

            for item in cart_items:

                if max_index_length < len(str(index)):
                    max_index_length = len(str(index))

                if max_product_id_length < len(item["id"]):
                    max_product_id_length = len(item["id"])

                if max_product_name_length < len(item["name"]):
                    max_product_name_length = len(item["name"])

                if max_quantity_length < len(str(item["number"])):
                    max_quantity_length = len(str(item["number"]))

                if max_price_length < len(f"{item['price']:,}đ"):
                    max_price_length = len(f"{item['price']:,}đ")

                item_total = item["number"] * item["price"]

                if max_total_length < len(f"{item_total:,}đ"):
                    max_total_length = len(f"{item_total:,}đ")

                index += 1

            header = (
                f"{index_header:<{max_index_length}} | "
                f"{product_id_header:<{max_product_id_length}} | "
                f"{product_name_header:<{max_product_name_length}} | "
                f"{quantity_header:<{max_quantity_length}} | "
                f"{price_header:<{max_price_length}} | "
                f"{total_header:<{max_total_length}}"
            )

            print(header)
            print("-" * (len(header) + 2))

            total_quantity = 0
            total_payment = 0

            index = 1

            for item in cart_items:

                item_total = item["number"] * item["price"]

                print(
                    f"{index:<{max_index_length}} | "
                    f"{item['id']:<{max_product_id_length}} | "
                    f"{item['name']:<{max_product_name_length}} | "
                    f"{item['number']:<{max_quantity_length}} | "
                    f"{item['price']:<{max_price_length},}đ | "
                    f"{item_total:<{max_total_length},}đ"
                )

                total_quantity += item["number"]
                total_payment += item_total

                index += 1

            print("-" * (len(header) + 2))

            print(f"\n=> Tổng số lượng sản phẩm trong giỏ hàng: {total_quantity}")
            print(f"=> Tổng tiền thành toán: {total_payment:,}VND\n")

        case "2":

            print("\n--- Thêm sản phẩm mới / Cộng dồn số lượng ---")

            product_id_input = input("Nhập mã sản phẩm: ").strip()
            product_name_input = input("Nhập tên sản phẩm: ").strip()

            quantity_input = int(input("Nhập số lượng: "))
            price_input = int(input("Nhập đơn giá: "))

            if quantity_input <= 0 or price_input < 0:
                print("Số lượng hoặc đơn giá không hợp lệ!")

            else:

                for item in cart_items:
                    if item["id"] == product_id_input:

                        item["number"] += quantity_input
                        print("Sản phẩm đã tồn tại -> Đã cộng dồn số lượng.")

                        break
                else:

                    cart_items.append({
                        "id": product_id_input,
                        "name": product_name_input,
                        "number": quantity_input,
                        "price": price_input
                    })

                    print("Đã thêm sản phẩm mới vào giỏ hàng.")

        case "3":

            print("\n--- Cập nhật số lượng sản phẩm ---")
            product_id_input = input("Nhập mã sản phẩm cần cập nhật: ").strip()
            new_quantity_input = int(input("Nhập số lượng mới: "))

            if new_quantity_input <= 0:
                print("Số lượng không hợp lệ!")

            else:
                for item in cart_items:
                    if item["id"] == product_id_input:

                        item["number"] = new_quantity_input
                        print("Cập nhật số lượng thành công.")

                        break

                else:
                    print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        case "4":

            print("\n--- Xóa sản phẩm khỏi giỏ hàng ---")
            product_id_input = input("Nhập mã sản phẩm cần xóa: ").strip()

            for item in cart_items:
                if item["id"] == product_id_input:

                    cart_items.remove(item)
                    print("Đã xóa sản phẩm khỏi giỏ hàng.")

                    break
            else:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        case "5":
            print("Thoát chương trình...")
            is_run_true = False
            
        case _:
            print("Chức năng bạn chọn không tồn tại!")