########
# Problem Statement:
#
# You are working on an e-commerce platform that has a discount system. There are multiple types of users: new users,
# loyal users, and VIP users. Each type of user is eligible for different discounts. You want to create a flexible
# and reusable solution to apply different discount rules to users based on their type. Use Python decorators to
# handle this logic.
#
# Requirements:
#
# 	1.	Create a base decorator apply_discount that:
# 	•	Takes the user type and the total bill amount as input.
# 	•	Applies different discount rules based on the usertype.
# 	2.	Apply specific discounts to the following user types:
# 	•	New users: Get a 5% discount on the total amount.
# 	•	Loyal users: Get a 10% discount on the total amount.
# 	•	VIP users: Get a 20% discount on the total amount.
# 	3.	Create functions that represent purchases:
# 	•	new_user_purchase(total): Represents a purchase by a new user.
# 	•	loyal_user_purchase(total): Represents a purchase by a loyal user.
# 	•	vip_user_purchase(total): Represents a purchase by a VIP user.
# 	4.	Each function should take in the total bill amount, and the decorator
#   	should apply the correct discount and
# 	print the final amount after discount.
#
# Task:
#
# 	•	Use the apply_discount decorator to dynamically apply the appropriate
#   	discount based on the user type when
# 	they make a purchase.
#
# Expected Output:
#
# 	•	When calling new_user_purchase(100), it should print the final amount after applying a 5% discount.
# 	•	When calling loyal_user_purchase(100), it should print the final amount after applying a 10% discount.
# 	•	When calling vip_user_purchase(100), it should print the final amount after applying a 20% discount.
#
# Let me know if you need help implementing this or have any questions!


from calculate_discount import apply_discount


@apply_discount(0.05)
def new_user_purchase(total_amount):
    return total_amount


@apply_discount(0.10)
def loyal_user_purchase(total_amount):
    return total_amount


@apply_discount(0.20)
def VIP_user_purchase(total_amount):
    return total_amount

if __name__ == '__main__':
    object = new_user_purchase(100)
    print(f"New user needs to pay {object}")

    vip_user = VIP_user_purchase(100)
    print("VIP user needs to pay", vip_user)

    loyal_user = loyal_user_purchase(100)
    print(f"loyal user needs to pay {loyal_user}")
