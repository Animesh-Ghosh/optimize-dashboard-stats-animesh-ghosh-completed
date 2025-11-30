# Task Overview
Shopboard is a lightweight analytics dashboard built for a small social network. As user activity has grown, the dashboard’s statistics and recent activity feeds have become noticeably slow to load — especially when users scroll through deeper pages. The database schema currently lacks essential foreign key constraints and indexes, causing performance bottlenecks and increasing the risk of data inconsistency.

## Guidance
- Dashboard stats and activity endpoints are already built and functional, but slow with increased data.
- Stats endpoint issues:
  - The current implementation runs multiple database queries sequentially, making the response noticeably slower as data volume increases.
  - Each request opens new database connections and performs heavy read operations, which impacts performance under higher load.
- Activity endpoint issues:
  - The current query design and data access patterns are not optimized for large datasets, leading to delays in response times.
  - The recent activity feed becomes progressively slower as users scroll through more data.
- Database lacks foreign key relationships between users, posts, comments, and sessions, risking data corruption.
- Tables don't have any indexes on columns often used for filtering or ordering .
- Your job: Optimize queries, add indexes and constraints, improve route handler performance and connection handling.

## Database Access
- Host: `<DROPLET_IP>`
- Port: 5432
- Database: shopboard_db
- Username: dashboard_admin
- Password: dash_pwd123

## Objectives
- Investigate and improve the response times of the dashboard statistics and recent activity endpoints, particularly under heavy data load or deep pagination
- Analyze the existing database schema and apply appropriate constraints and optimizations to ensure data consistency and faster lookups
- Review query patterns and implement improvements that reduce redundant operations and unnecessary data fetching
- Enhance database connection handling within the API to ensure efficient resource usage and minimal overhead
- Refactor database code to reuse a single DB connection per request rather than per query
- Introduce basic defensive handling around database calls to ensure failures produce clear, correct API responses.


## How to Verify
- Try calling the dashboard stats endpoint with a typical dataset and observe whether the response feels noticeably faster compared to the original behavior.
- Scroll deeper through the recent activity feed and check whether later pages respond more smoothly after your refinements.
- Insert or update sample data to confirm that key relationships between tables are now protected by constraints.
- Use SQL inspection or query analysis tools to see whether the most frequently accessed queries start using the intended indexes more consistently.
- Trigger the endpoints under modest concurrent load to confirm database connections behave predictably and errors surface cleanly without crashing the API.
