CREATE TABLE customers (
  customer_id varchar(255) PRIMARY KEY,
  customer_unique_id varchar(255) NOT NULL,
  customer_zip_code_prefix varchar(20),
  customer_city varchar(255),
  customer_state varchar(5)
);

CREATE TABLE orders (
  order_id varchar(255) PRIMARY KEY,
  customer_id varchar(255) NOT NULL,
  order_status varchar(255),
  order_purchase_timestamp timestamp,
  order_approved_at timestamp,
  order_delivered_carrier_date timestamp,
  order_delivered_customer_date timestamp,
  order_estimated_delivery_date timestamp,
  CONSTRAINT fk_customer_order FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);

CREATE TABLE sellers (
  seller_id varchar(255) PRIMARY KEY,
  seller_zip_code_prefix varchar(20),
  seller_city varchar(255),
  seller_state varchar(5)
);

CREATE TABLE products (
  product_id varchar(255) PRIMARY KEY,
  product_category_name varchar(255),
  product_name_lenght int,
  product_description_lenght int,
  product_photos_qty int,
  product_weight_g int,
  product_length_cm int,
  product_height_cm int,
  product_width_cm int
);

CREATE TABLE order_items (
  order_id varchar(255) NOT NULL,
  order_item_id int NOT NULL,
  product_id varchar(255) NOT NULL,
  seller_id varchar(255) NOT NULL,
  shipping_limit_date timestamp,
  price numeric,
  freight_value numeric,
  PRIMARY KEY (order_id, order_item_id),
  CONSTRAINT fk_order_item_order FOREIGN KEY (order_id)
    REFERENCES orders(order_id),
  CONSTRAINT fk_order_item_product FOREIGN KEY (product_id)
    REFERENCES products(product_id),
  CONSTRAINT fk_order_item_seller FOREIGN KEY (seller_id)
    REFERENCES sellers(seller_id)
);

CREATE TABLE order_payments (
  order_id varchar(255),
  payment_sequential int,
  payment_type varchar(255),
  payment_installments int,
  payment_value numeric,
  PRIMARY KEY (order_id, payment_sequential),
  CONSTRAINT fk_payment_order FOREIGN KEY (order_id)
    REFERENCES orders(order_id)
);

CREATE TABLE order_reviews (
  review_id varchar(255),
  order_id varchar(255) NOT NULL,
  review_score int,
  review_comment_title varchar(255),
  review_comment_message text,
  review_creation_date timestamp,
  review_answer_timestamp timestamp,
  PRIMARY KEY (review_id, order_id),
  CONSTRAINT fk_review_order FOREIGN KEY (order_id)
    REFERENCES orders(order_id)
);