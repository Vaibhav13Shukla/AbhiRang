CREATE TABLE user (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone_number TEXT NOT NULL,
    user_type TEXT NOT NULL, -- artist, buyer, admin
    is_verified BOOLEAN DEFAULT 0 -- for artist verification
);

CREATE TABLE category (
    category_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE product (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL,
    stock_quantity INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    artist_id INTEGER NOT NULL,
    rating REAL CHECK(rating >= 0 AND rating <= 5),
    dimensions TEXT, -- e.g., "24x36 in"
    medium TEXT, -- e.g., "oil on canvas"
    image_url TEXT, -- URL for displaying the artwork
    FOREIGN KEY (category_id) REFERENCES category(category_id),
    FOREIGN KEY (artist_id) REFERENCES user(user_id)
);

CREATE TABLE Cart (
    cart_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE Cart_Item (
    cart_item_id INTEGER PRIMARY KEY,
    cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price_per_unit REAL NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE "Order" (
    order_id INTEGER   
 PRIMARY KEY,
    user_id INTEGER NOT NULL,
    order_date DATETIME NOT NULL,
    total_amount REAL NOT NULL,
    order_status TEXT NOT NULL, -- e.g., pending, completed, canceled
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE Order_Item (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price_per_unit   
 REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES "Order"(order_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE   
 Commission (
    commission_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL, -- buyer
    artist_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    agreed_price REAL CHECK(agreed_price >= 0),
    status TEXT NOT NULL, -- pending, in progress, completed
    deadline DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (artist_id) REFERENCES user(user_id)
);

CREATE TABLE Insurance (
    insurance_id INTEGER PRIMARY KEY,
    commission_id INTEGER,
    is_insured BOOLEAN DEFAULT 0,
    coverage_details TEXT,
    price REAL CHECK(price >= 0),
    terms TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (commission_id) REFERENCES Commission(commission_id)
);

CREATE TABLE Review (
    review_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    rating REAL CHECK(rating >= 0 AND rating <= 5),
    comment TEXT,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

CREATE TABLE Artist_Portfolio (
    portfolio_id INTEGER PRIMARY KEY,
    artist_id INTEGER NOT NULL,
    artwork_name TEXT NOT NULL,
    description TEXT NOT NULL,
    medium TEXT,
    image_url TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES user(user_id)
);