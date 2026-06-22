class SchemaService:

    @staticmethod
    def get_schema_context():

        return """
        TABLE customers (
            customer_id,
            customer_name,
            segment,
            city,
            state,
            country
        )

        TABLE products (
            product_id,
            category,
            sub_category,
            product_name
        )

        TABLE orders (
            order_id,
            customer_id,
            product_id,
            order_date,
            sales,
            profit,
            discount,
            quantity
        )

        RELATIONSHIPS:

        orders.customer_id = customers.customer_id
        orders.product_id = products.product_id
        """