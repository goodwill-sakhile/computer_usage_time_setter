using CafeTimeManager.Core.Models;
using Microsoft.EntityFrameworkCore;

namespace CafeTimeManager.Data.Context
{
    public class AppDbContext : DbContext
    {
        public DbSet<User> Users { get; set; }
        public DbSet<Admin> Admins { get; set; }

        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) {}

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            // Seed admin
            modelBuilder.Entity<Admin>().HasData(new Admin
            {
                Username = "admin",
                PasswordHash = Convert.ToBase64String(
                    System.Security.Cryptography.SHA256.Create()
                    .ComputeHash(System.Text.Encoding.UTF8.GetBytes("admin123"))
                )
            });
        }
    }
}
