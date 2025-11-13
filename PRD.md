# ABHIRANG: Story-First Curated Art Gallery Platform
## Object-Oriented Programming Project Proposal

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Personal Motivation](#2-personal-motivation)
3. [Problem Statement](#3-problem-statement)
4. [Requirements Specification](#4-requirements-specification)
5. [System Architecture](#5-system-architecture)
6. [Features Table](#6-features-table)
7. [User Interaction Flow](#7-user-interaction-flow)
8. [Technology Stack](#8-technology-stack)
9. [SOLID Principles Application](#9-solid-principles-application)
10. [Domain Model & Class Design](#10-domain-model--class-design)
11. [Project Timeline](#11-project-timeline)
12. [Expected Deliverables](#12-expected-deliverables)

---

## 1. Project Overview

### 1.1 Project Name
**ABHIRANG** - A Curated Art Gallery Platform

### 1.2 Project Description
ABHIRANG is a web-based curated art gallery platform that revolutionizes online art discovery by placing artist stories and creative journeys at the center of the buying experience. Unlike mass marketplaces, ABHIRANG features only carefully selected artworks, each accompanied by rich narratives that help buyers form emotional connections with art.

The platform serves three primary user types:
- **Art Buyers**: Individuals seeking meaningful art with authentic stories
- **Artists**: Creators wanting to showcase their work with narrative context
- **Curators/Admins**: Platform managers who control quality and catalog

### 1.3 Core Value Proposition
Traditional online art marketplaces overwhelm users with volume and lack context about the creative process. ABHIRANG solves this by:
- Curating a selective catalog of high-quality artworks
- Emphasizing the "why" behind each piece through storytelling
- Providing detailed artist profiles that build trust and connection
- Offering visualization tools to preview art in personal spaces

### 1.4 Project Scope
This is a **full-stack web application** that will be built from scratch, demonstrating:
- Clean architecture with Domain-Driven Design
- SOLID principles throughout the codebase
- Object-oriented design patterns
- Layered architecture (Domain → Application → Infrastructure)
- Modern web technologies with type safety
- Persistent data storage
- User authentication and authorization
- File upload and storage capabilities

---

## 2. Personal Motivation

### 2.1 Why This Project?
As a student passionate about the intersection of technology and creative industries, I've observed how online art marketplaces have become increasingly transactional. Artists are reduced to product listings, and buyers miss the emotional context that makes art meaningful.

**Personal Drivers:**

1. **Creator Economy Interest**: I'm deeply interested in platforms that empower creators. ABHIRANG aligns with my broader goal of building technology that gives artists better tools to connect with audiences.

2. **Technical Challenge**: This project allows me to demonstrate advanced OOP concepts, clean architecture, and modern full-stack development in a real-world context that goes beyond CRUD applications.

3. **Design Excellence**: I want to showcase how thoughtful software architecture—applying SOLID principles, design patterns, and clean code—creates maintainable, extensible systems.

4. **Portfolio Value**: This project serves as a substantial portfolio piece that demonstrates both technical depth (architecture, design patterns) and product thinking (user experience, business logic).

### 2.2 Learning Objectives
Through this project, I aim to:
- Apply SOLID principles in a complex, real-world domain
- Implement Domain-Driven Design with clear bounded contexts
- Use design patterns appropriately (Repository, Factory, Strategy, Observer)
- Build a layered architecture that separates concerns effectively
- Create a system that's testable, maintainable, and extensible
- Demonstrate professional-grade code organization and documentation

---

## 3. Problem Statement

### 3.1 Problem Domain
**Online art purchasing lacks emotional connection and context.**

Current Challenges:
- **For Buyers**: Mass marketplaces feel overwhelming and transactional; difficult to understand the story behind artwork; uncertainty about quality and authenticity
- **For Artists**: Lost in volume on open platforms; no way to convey creative process; difficulty building audience connection
- **For Curators**: No efficient tools to manage quality-focused galleries; manual processes for artwork management

### 3.2 Proposed Solution
A curated platform where:
- Only selected artworks are published (quality over quantity)
- Every piece includes a detailed creative story
- Artist profiles provide narrative depth
- Admin tools enable efficient curation
- Buyers can visualize art in their spaces

### 3.3 Target Users

**Primary Users:**
1. **Art Buyers** (Ages 25-40, urban professionals)
   - Want art with personal meaning
   - Value authenticity and story
   - Willing to pay premium for quality

2. **Independent Artists** (Ages 22-50, 2-10 years experience)
   - Seek platforms that respect creative process
   - Want to build authentic audience connections
   - Desire fair presentation and brand control

3. **Platform Curator/Admin**
   - Maintains quality standards
   - Manages artwork catalog
   - Monitors platform health

### 3.4 Constraints
- 3-day development timeline (proof of concept)
- Individual project (no team collaboration)
- Must demonstrate OOP and SOLID principles
- Must include persistence layer
- Must have functional UI

---

## 4. Requirements Specification

### 4.1 Functional Requirements

#### FR1: User Authentication & Authorization
- Users can sign up and log in using email/password
- Support for OAuth (Google) authentication
- Role-based access control (Buyer vs. Admin)
- Session management and secure logout

#### FR2: Public Gallery
- Display all published artworks in responsive grid
- Show artwork preview with title, artist, price, story snippet
- Filter artworks by artist (future: by price, medium, tags)
- Click artwork card to view details

#### FR3: Artwork Detail Page
- Display high-resolution artwork image
- Show complete artist story (200-500 words)
- Display artwork metadata (dimensions, medium, price)
- Link to artist profile
- Add to cart functionality
- Optional: Process images carousel

#### FR4: Artist Profile Pages
- Display artist biography and photo
- Show artist's creative approach
- List all artworks by the artist
- Include social media links

#### FR5: Shopping Cart
- Add/remove artworks to cart
- Persist cart across sessions (localStorage for MVP)
- Display cart summary with total
- Proceed to checkout

#### FR6: Checkout & Orders
- Collect shipping information
- Process payment (Stripe test mode)
- Create order record in database
- Send order confirmation email
- Store order history

#### FR7: Admin Dashboard
- Protected route (admin-only access)
- View all artworks (published/unpublished)
- Create new artwork with:
  - Title, story, medium, dimensions, price
  - Image upload (main + process images)
  - Artist selection
  - Tags/categories
- Edit/delete existing artworks
- Manage artist profiles (create, edit, deactivate)
- View orders list

### 4.2 Non-Functional Requirements

#### NFR1: Architecture
- **Layered Architecture**: Clear separation of Domain, Application, and Infrastructure layers
- **Domain-Driven Design**: Rich domain models with business logic
- **Dependency Inversion**: High-level modules don't depend on low-level modules

#### NFR2: SOLID Principles
- **Single Responsibility**: Each class has one reason to change
- **Open/Closed**: Open for extension, closed for modification
- **Liskov Substitution**: Subtypes can replace base types
- **Interface Segregation**: Clients shouldn't depend on unused interfaces
- **Dependency Inversion**: Depend on abstractions, not concretions

#### NFR3: Code Quality
- Type-safe implementation (TypeScript)
- Meaningful naming conventions
- Small, focused classes and methods
- Minimal code duplication
- Comprehensive error handling
- Input validation at all entry points

#### NFR4: Performance
- Page load times under 2 seconds
- Optimized image delivery
- Lazy loading for images
- Responsive design (mobile-first)

#### NFR5: Security
- Secure authentication (no plain-text passwords)
- Protected admin routes
- Input sanitization to prevent injection attacks
- HTTPS enforcement
- Secure payment processing (PCI compliant via Stripe)

#### NFR6: Persistence
- Relational data storage (Convex database)
- File storage for images (Convex storage)
- Data consistency and integrity
- Backup and recovery capability

#### NFR7: Maintainability
- Clear project structure
- Comprehensive documentation
- Modular, reusable components
- Easy to test (unit and integration tests)
- Version control (Git)

---

## 5. System Architecture

### 5.1 Architectural Style
**Clean Architecture** with **Layered Design**

The system follows a three-tier architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────┐
│         Presentation Layer (UI)             │
│  (Next.js Pages, React Components)          │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│        Application Layer                    │
│  (Use Cases, Service Orchestration)         │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│          Domain Layer                       │
│  (Entities, Value Objects, Domain Logic)    │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│      Infrastructure Layer                   │
│  (Repositories, External Services, DB)      │
└─────────────────────────────────────────────┘
```

### 5.2 Layer Responsibilities

#### **Domain Layer** (Core Business Logic)
**Purpose**: Contains the business rules and domain entities

**Components**:
- `Artwork` entity (artwork details, story, pricing)
- `Artist` entity (profile, bio, works)
- `Order` entity (order details, status)
- `Cart` value object (cart items, totals)
- `User` entity (authentication, roles)
- Domain services (pricing calculator, validation)

**Key Characteristics**:
- No dependencies on outer layers
- Pure business logic
- Framework-independent
- Highly testable

#### **Application Layer** (Use Cases)
**Purpose**: Orchestrates domain objects to fulfill use cases

**Components**:
- `CreateArtworkUseCase` - Handle artwork creation with validation
- `PublishArtworkUseCase` - Publish artwork to gallery
- `AddToCartUseCase` - Manage cart operations
- `CheckoutUseCase` - Process order creation
- `GetArtworkDetailsUseCase` - Retrieve artwork with artist info
- `ListGalleryArtworksUseCase` - Get all published artworks
- Service interfaces (defined here, implemented in infrastructure)

**Key Characteristics**:
- Coordinates domain objects
- Defines service interfaces
- Transaction boundaries
- Authorization checks

#### **Infrastructure Layer** (External Concerns)
**Purpose**: Implements technical capabilities and external integrations

**Components**:
- `ConvexArtworkRepository` - Data persistence implementation
- `ConvexArtistRepository` - Artist data access
- `ConvexOrderRepository` - Order storage
- `ClerkAuthService` - Authentication implementation
- `StripePaymentService` - Payment processing
- `ConvexFileStorage` - Image upload/storage
- Email service implementation

**Key Characteristics**:
- Implements repository interfaces from application layer
- Handles external API calls
- Database queries and transactions
- File I/O operations

#### **Presentation Layer** (UI)
**Purpose**: User interface and interaction

**Components**:
- Next.js pages (routing)
- React components (UI)
- Forms and validation
- State management
- API route handlers

**Key Characteristics**:
- Calls application layer use cases
- Displays data to users
- Handles user input
- Minimal business logic

### 5.3 Design Patterns Applied

#### Repository Pattern
**Purpose**: Abstract data access logic

```typescript
// Domain defines the interface
interface IArtworkRepository {
  findById(id: string): Promise<Artwork | null>;
  findAll(): Promise<Artwork[]>;
  save(artwork: Artwork): Promise<Artwork>;
  delete(id: string): Promise<void>;
}

// Infrastructure implements it
class ConvexArtworkRepository implements IArtworkRepository {
  // Implementation details...
}
```

#### Factory Pattern
**Purpose**: Create complex domain objects

```typescript
class ArtworkFactory {
  static create(data: CreateArtworkDTO): Artwork {
    // Validation and creation logic
    return new Artwork({
      title: data.title,
      story: data.story,
      price: Money.fromINR(data.price),
      dimensions: new Dimensions(data.height, data.width),
      // ...
    });
  }
}
```

#### Strategy Pattern
**Purpose**: Interchangeable algorithms (e.g., pricing strategies)

```typescript
interface IPricingStrategy {
  calculatePrice(basePrice: number): number;
}

class StandardPricing implements IPricingStrategy {
  calculatePrice(basePrice: number): number {
    return basePrice;
  }
}

class DiscountPricing implements IPricingStrategy {
  calculatePrice(basePrice: number): number {
    return basePrice * 0.9; // 10% discount
  }
}
```

#### Service Layer Pattern
**Purpose**: Encapsulate business logic operations

```typescript
class ArtworkService {
  constructor(
    private artworkRepo: IArtworkRepository,
    private artistRepo: IArtistRepository
  ) {}

  async getArtworkWithArtist(id: string): Promise<ArtworkDTO> {
    const artwork = await this.artworkRepo.findById(id);
    const artist = await this.artistRepo.findById(artwork.artistId);
    return this.mapToDTO(artwork, artist);
  }
}
```

---

## 6. Features Table

| Feature | Priority | User Type | Description | SOLID Principle Demonstrated |
|---------|----------|-----------|-------------|------------------------------|
| **User Authentication** | P0 | All | Sign up, login, OAuth integration, session management | SRP: Separate auth logic; DIP: Auth service interface |
| **Public Gallery Grid** | P0 | Buyer | Browse all published artworks in responsive grid with previews | OCP: Extensible filtering; SRP: Separate display logic |
| **Artwork Detail View** | P0 | Buyer | View high-res image, read full story, see artist info, pricing | SRP: Separate data fetching from display |
| **Story Module** | P0 | Buyer | Rich text display of artist's creative narrative | SRP: Story rendering separate from artwork logic |
| **Artist Profile Page** | P0 | Buyer | View artist bio, creative approach, and all their artworks | SRP: Artist data separate from artwork data |
| **Shopping Cart** | P0 | Buyer | Add/remove items, persist cart, view totals | SRP: Cart logic separate; ISP: Cart interface |
| **Checkout & Payment** | P0 | Buyer | Enter shipping info, process payment via Stripe, confirm order | DIP: Payment service abstraction; SRP: Order creation |
| **Admin Dashboard** | P0 | Admin | View all artworks, manage published status | SRP: Admin UI separate from business logic |
| **Artwork Upload** | P0 | Admin | Create new artwork with images, story, metadata | SRP: Upload separate from validation; OCP: Extensible validation |
| **Artist Management** | P0 | Admin | Create/edit artist profiles with bio and images | SRP: Artist CRUD separate from artwork |
| **Image Upload** | P0 | Admin | Upload and store artwork images (main + process) | DIP: Storage service abstraction; SRP: File handling separate |
| **Order Management** | P1 | Admin | View all orders, update order status | SRP: Order view separate from order processing |
| **Role-Based Access** | P0 | System | Restrict admin routes to authorized users | SRP: Authorization middleware separate |
| **Data Persistence** | P0 | System | Store artworks, artists, orders, users in database | DIP: Repository pattern; LSP: Repository implementations |
| **Email Notifications** | P1 | System | Send order confirmation emails | DIP: Email service interface; SRP: Separate notification logic |
| **Preview on Wall** | P2 | Buyer | Upload room photo, overlay artwork for visualization | OCP: Extensible to AR; SRP: Separate image processing |

**Priority Levels:**
- **P0**: MVP blocker (must have)
- **P1**: Important for complete experience
- **P2**: Nice to have, can be added post-MVP

---

## 7. User Interaction Flow

### 7.1 Buyer Journey

#### Flow 1: Discover and Purchase Artwork

```
1. User lands on homepage
   └─> Sees gallery grid with artwork cards
   
2. User browses gallery
   └─> Filters by artist (optional)
   └─> Clicks on artwork card
   
3. User views artwork detail page
   └─> Reads full story
   └─> Views high-res image
   └─> Checks dimensions and price
   └─> Clicks "View Artist Profile" (optional)
   
4. User explores artist profile
   └─> Reads artist bio
   └─> Views other artworks by same artist
   └─> Returns to artwork detail
   
5. User adds artwork to cart
   └─> Cart icon updates with count
   └─> Notification: "Added to cart"
   
6. User proceeds to cart
   └─> Reviews items
   └─> Clicks "Checkout"
   
7. User completes checkout
   └─> Logs in (if not already)
   └─> Enters shipping address
   └─> Enters payment details
   └─> Submits order
   
8. User receives confirmation
   └─> Order confirmation page displayed
   └─> Email confirmation sent
   └─> Order stored in database
```

**Key Interactions:**
- **Homepage**: Click artwork card → Navigate to detail
- **Artwork Detail**: Click "Add to Cart" → Item added, notification shown
- **Cart**: Click "Remove" → Item deleted, totals updated
- **Checkout**: Submit form → Validation → Payment processing → Confirmation

---

### 7.2 Admin Journey

#### Flow 2: Upload and Publish Artwork

```
1. Admin logs in
   └─> Redirected to admin dashboard
   
2. Admin views dashboard
   └─> Sees list of all artworks
   └─> Clicks "Add New Artwork"
   
3. Admin fills artwork form
   └─> Enters title, story (rich text)
   └─> Selects artist from dropdown
   └─> Enters dimensions, medium, price
   └─> Adds tags
   
4. Admin uploads images
   └─> Drags/clicks to upload main image
   └─> Progress indicator shows upload status
   └─> Uploads 2-4 process images (optional)
   
5. Admin previews artwork
   └─> Clicks "Preview" button
   └─> Sees how artwork page will look
   └─> Reviews story formatting
   
6. Admin publishes artwork
   └─> Clicks "Publish" button
   └─> Validation runs
   └─> Artwork saved to database
   └─> Images uploaded to storage
   └─> Confirmation shown
   
7. Artwork appears in public gallery
   └─> Admin verifies on gallery page
```

**Key Interactions:**
- **Dashboard**: Click "Add New Artwork" → Form opens
- **Upload Form**: Drag-drop image → Upload progress → Success indicator
- **Rich Text Editor**: Format story text → Bold, italic, paragraphs
- **Preview**: Click "Preview" → Modal shows artwork detail view
- **Publish**: Click "Publish" → Validation → Save → Confirmation

---

### 7.3 Artist Profile Viewing

#### Flow 3: Explore Artist

```
1. User clicks artist name (from artwork detail)
   └─> Navigates to artist profile page
   
2. User views artist header
   └─> Sees profile photo and name
   └─> Reads short bio (2-3 sentences)
   
3. User reads detailed bio
   └─> Expands "About" section
   └─> Reads 200-400 word narrative
   └─> Learns about creative approach
   
4. User views artist's works
   └─> Scrolls down to artwork grid
   └─> Sees all pieces by this artist
   └─> Clicks artwork → Goes to detail page
   
5. User follows artist (future)
   └─> Clicks social media links
   └─> Visits Instagram/website
```

**Key Interactions:**
- **Artist Link**: Click name → Navigate to profile
- **Expandable Bio**: Click "Read More" → Full bio expands
- **Artwork Grid**: Click artwork card → Navigate to detail
- **Social Links**: Click icon → Open in new tab

---

### 7.4 Cart Management

#### Flow 4: Modify Cart

```
1. User adds artwork to cart
   └─> Cart icon shows item count
   
2. User clicks cart icon
   └─> Navigates to cart page
   
3. User reviews cart
   └─> Sees artwork thumbnail, title, artist, price
   └─> Views subtotal
   
4. User removes item (optional)
   └─> Clicks "Remove" button
   └─> Item deleted from cart
   └─> Totals recalculated
   └─> UI updates immediately
   
5. User proceeds to checkout
   └─> Clicks "Proceed to Checkout"
   └─> If not logged in → Redirected to login
   └─> If logged in → Navigates to checkout
```

**Key Interactions:**
- **Add to Cart**: Button click → Add item → Update count → Show notification
- **Remove**: Click "Remove" → Confirm (optional) → Delete → Update UI
- **Checkout**: Click button → Auth check → Navigate

---

### 7.5 Admin Artist Management

#### Flow 5: Create Artist Profile

```
1. Admin navigates to Artists page
   └─> Views table of all artists
   └─> Clicks "Add New Artist"
   
2. Admin fills artist form
   └─> Enters name
   └─> Uploads profile photo
   └─> Writes short bio (200 chars)
   └─> Writes long bio (rich text, 400 chars)
   └─> Adds creative approach (optional)
   └─> Enters social media URLs
   
3. Admin saves artist
   └─> Clicks "Save" button
   └─> Validation runs
   └─> Artist saved to database
   └─> Slug generated (URL-friendly name)
   └─> Confirmation shown
   
4. Artist available for artwork assignment
   └─> Appears in artist dropdown on artwork form
```

**Key Interactions:**
- **Artists Page**: Click "Add New Artist" → Form opens
- **Profile Photo**: Upload image → Crop to circle → Preview
- **Rich Text**: Write bio → Format text → Preview
- **Save**: Click "Save" → Validate → Store → Confirm

---

## 8. Technology Stack

### 8.1 Technology Choices with Justification

#### **Frontend Framework: Next.js 14+ (App Router)**

**Why Next.js?**
- **Server-Side Rendering**: Improves SEO for artwork pages
- **App Router**: Modern file-based routing with layouts
- **Image Optimization**: Automatic image optimization and lazy loading
- **TypeScript Support**: First-class TypeScript integration
- **API Routes**: Built-in backend API capabilities

**OOP Relevance**: Component-based architecture follows composition principles

#### **Programming Language: TypeScript**

**Why TypeScript?**
- **Type Safety**: Catches errors at compile time
- **OOP Support**: Classes, interfaces, abstract classes, generics
- **Better Tooling**: IntelliSense, refactoring support
- **Self-Documenting**: Types serve as documentation
- **SOLID Enforcement**: Interfaces enforce contracts

**OOP Relevance**: Full support for OOP paradigms, interface-based design

#### **UI Framework: React with Tailwind CSS + shadcn/ui**

**Why This Stack?**
- **React**: Component reusability, unidirectional data flow
- **Tailwind**: Utility-first CSS, rapid prototyping, consistent design
- **shadcn/ui**: Pre-built accessible components following best practices

**OOP Relevance**: Component composition, encapsulation of UI logic

#### **Backend: Convex**

**Why Convex?**
- **Serverless**: No infrastructure management
- **Type-Safe**: TypeScript-first API
- **Real-Time**: WebSocket support for future features
- **File Storage**: Built-in file upload and storage
- **Database**: NoSQL with strong query capabilities
- **Schema Validation**: Enforced data structure

**OOP Relevance**: Clear separation of data layer, repository pattern implementation

#### **Authentication: Clerk**

**Why Clerk?**
- **Secure**: Industry-standard security practices
- **Role Management**: Built-in RBAC (Role-Based Access Control)
- **OAuth**: Google, Apple sign-in out of the box
- **Session Management**: Handled automatically
- **Next.js Integration**: Excellent SDK for Next.js

**OOP Relevance**: Dependency inversion (auth service interface)

#### **Payment Processing: Stripe**

**Why Stripe?**
- **PCI Compliant**: Handles payment security
- **Test Mode**: Easy development and testing
- **Webhooks**: Event-driven order confirmation
- **Well-Documented**: Comprehensive API documentation
- **TypeScript SDK**: Type-safe integration

**OOP Relevance**: Service abstraction, strategy pattern for payment methods

#### **Deployment: Vercel**

**Why Vercel?**
- **Next.js Optimized**: Built by the Next.js team
- **Automatic Deployments**: Push to Git → Deploy
- **Edge Functions**: Fast, globally distributed
- **Preview Deployments**: Every PR gets a preview URL
- **Zero Config**: Works out of the box

---

### 8.2 Tech Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Next.js 14 + React | UI framework with SSR |
| **Language** | TypeScript | Type-safe development |
| **Styling** | Tailwind CSS + shadcn/ui | Rapid UI development |
| **Backend** | Convex | Database + serverless functions |
| **Auth** | Clerk | User authentication & authorization |
| **Payment** | Stripe | Payment processing |
| **Storage** | Convex Storage | File upload/storage |
| **Deployment** | Vercel | Hosting + CI/CD |
| **Version Control** | Git + GitHub | Source code management |

---

## 9. SOLID Principles Application

### 9.1 Single Responsibility Principle (SRP)

**Definition**: A class should have only one reason to change.

**Application in ABHIRANG**:

#### Example 1: Artwork Entity
```typescript
// ❌ BAD: Artwork doing too much
class Artwork {
  id: string;
  title: string;
  price: number;
  
  save() { /* database logic */ }
  sendEmail() { /* email logic */ }
  uploadImage() { /* file logic */ }
}

// ✅ GOOD: Single responsibility
class Artwork {
  // Domain entity - only business logic
  id: string;
  title: string;
  price: Money;
  
  calculateDiscountedPrice(percentage: number): Money {
    return this.price.multiply(1 - percentage);
  }
  
  isPublishable(): boolean {
    return this.title.length > 0 && this.story.length >= 150;
  }
}

// Separate repository for persistence
class ArtworkRepository {
  async save(artwork: Artwork): Promise<void> {
    // Database logic
  }
}

// Separate service for notifications
class EmailService {
  async sendOrderConfirmation(order: Order): Promise<void> {
    // Email logic
  }
}

// Separate service for file handling
class FileStorageService {
  async uploadImage(file: File): Promise<string> {
    // Upload logic
  }
}
```

**Benefits**: Each class has one reason to change. Artwork changes only when business rules change. Repository changes when database changes. Email service changes when email provider changes.

---

### 9.2 Open/Closed Principle (OCP)

**Definition**: Classes should be open for extension but closed for modification.

**Application in ABHIRANG**:

#### Example 2: Pricing Strategy
```typescript
// Base interface (closed for modification)
interface IPricingStrategy {
  calculatePrice(artwork: Artwork): number;
}

// Standard pricing (extension)
class StandardPricing implements IPricingStrategy {
  calculatePrice(artwork: Artwork): number {
    return artwork.basePrice;
  }
}

// Discount pricing (extension without modifying existing code)
class DiscountPricing implements IPricingStrategy {
  constructor(private discountPercent: number) {}
  
  calculatePrice(artwork: Artwork): number {
    return artwork.basePrice * (1 - this.discountPercent);
  }
}

// VIP pricing (new extension added later)
class VIPPricing implements IPricingStrategy {
  calculatePrice(artwork: Artwork): number {
    return artwork.basePrice * 0.8; // 20% discount for VIP
  }
}

// Client code (never needs to change)
class PriceCalculator {
  constructor(private strategy: IPricingStrategy) {}
  
  getPrice(artwork: Artwork): number {
    return this.strategy.calculatePrice(artwork);
  }
}
```

**Benefits**: New pricing strategies can be added without modifying existing code. System is extensible.

---

### 9.3 Liskov Substitution Principle (LSP)

**Definition**: Subtypes must be substitutable for their base types.

**Application in ABHIRANG**:

#### Example 3: Repository Implementations
```typescript
// Base interface defining contract
interface IArtworkRepository {
  findById(id: string): Promise<Artwork | null>;
  findAll(): Promise<Artwork[]>;
  save(artwork: Artwork): Promise<Artwork>;
  delete(id: string): Promise<void>;
}

// Convex implementation
class ConvexArtworkRepository implements IArtworkRepository {
  async findById(id: string): Promise<Artwork | null> {
    const doc = await this.convex.query(api.artworks.get, { id });
    return doc ? this.mapToDomain(doc) : null;
  }
  
  async findAll(): Promise<Artwork[]> {
    const docs = await this.convex.query(api.artworks.list);
    return docs.map(this.mapToDomain);
  }
  
  async save(artwork: Artwork): Promise<Artwork> {
    const dto = this.mapToDTO(artwork);
    const saved = await this.convex.mutation(api.artworks.create, dto);
    return this.mapToDomain(saved);
  }
  
  async delete(id: string): Promise<void> {
    await this.convex.mutation(api.artworks.delete, { id });
  }
}

// In-memory implementation for testing
class InMemoryArtworkRepository implements IArtworkRepository {
  private artworks: Map<string, Artwork> = new Map();
  
  async findById(id: string): Promise<Artwork | null> {
    return this.artworks.get(id) || null;
  }
  
  async findAll(): Promise<Artwork[]> {
    return Array.from(this.artworks.values());
  }
  
  async save(artwork: Artwork): Promise<Artwork> {
    this.artworks.set(artwork.id, artwork);
    return artwork;
  }
  
  async delete(id: string): Promise<void> {
    this.artworks.delete(id);
  }
}

// Client code works with either implementation
class ArtworkService {
  constructor(private repo: IArtworkRepository) {}
  
  async getAllArtworks(): Promise<Artwork[]> {
    return this.repo.findAll(); // Works with any implementation
  }
}
```
