# Little Lemon Restaurant API

## API Testing Routes

### Authentication
- POST /auth/users/ - Create new user
- POST /auth/token/login/ - Get authentication token  
- POST /auth/token/logout/ - Logout
- POST /restaurant/api-token-auth/ - Get authentication token (Django REST Framework)

### Menu Items
- GET /restaurant/menu/ - List all menu items
- POST /restaurant/menu/ - Create new menu item (requires authentication)
- GET /restaurant/menu/{id} - Get specific menu item
- PUT /restaurant/menu/{id} - Update menu item (requires authentication)
- PATCH /restaurant/menu/{id} - Partial update of menu item (requires authentication)
- DELETE /restaurant/menu/{id} - Delete menu item (requires authentication)

### Bookings
- GET /restaurant/booking/tables/ - List all bookings
- POST /restaurant/booking/tables/ - Create new booking (requires authentication)
- GET /restaurant/booking/tables/{id}/ - Get specific booking
- PUT /restaurant/booking/tables/{id}/ - Update booking (requires authentication)
- PATCH /restaurant/booking/tables/{id}/ - Partial update of booking (requires authentication)
- DELETE /restaurant/booking/tables/{id}/ - Delete booking (requires authentication)

### Home Page
- GET /restaurant/ - Restaurant home page