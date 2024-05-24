CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE public.customer (
    customer_id     uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    customer_no     VARCHAR(255),
    gender_id       uuid,
	age             INT
);

CREATE TABLE public.invoice (
	invoice_id       uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    invoice_no       VARCHAR(255),
    invoice_date     TIMESTAMP,
    total            VARCHAR(250),
    customer_id      uuid,
    payment_id       uuid,
    category_id      uuid,
    shopping_mall_id uuid
);

CREATE TABLE public.payment (
    payment_id      uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	payment_method  VARCHAR(255),
    label           serial,
	quantity        INT,
    price           DECIMAL
);

CREATE TABLE public.category (
    category_id     uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	category        VARCHAR(250),
    label           serial
);

CREATE TABLE public.shopping_mall (
    shopping_mall_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    shopping_mall   VARCHAR(250),
    label           serial
);

CREATE TABLE public.gender (
    gender_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    gender    VARCHAR(250),
    label     serial
);

ALTER TABLE public.invoice
    ADD CONSTRAINT fk_id_customer FOREIGN KEY (customer_id) REFERENCES public.customer (customer_id);

ALTER TABLE public.invoice
    ADD CONSTRAINT fk_id_category FOREIGN KEY (category_id) REFERENCES public.category (category_id);

ALTER TABLE public.customer
    ADD CONSTRAINT fk_id_gender FOREIGN KEY (gender_id) REFERENCES public.gender (gender_id);

ALTER TABLE public.invoice
    ADD CONSTRAINT fk_id_shopping_mall FOREIGN KEY (shopping_mall_id) REFERENCES public.shopping_mall (shopping_mall_id); 
    
ALTER TABLE public.invoice
    ADD CONSTRAINT fk_id_payment FOREIGN KEY (payment_id) REFERENCES public.payment (payment_id);