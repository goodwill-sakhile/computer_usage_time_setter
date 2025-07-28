using System.Security.Cryptography;
using System.Text;

namespace CafeTimeManager.Common.Helpers
{
    public static class PasswordHasher
    {
        public static string Hash(string password)
        {
            using var sha = SHA256.Create();
            byte[] bytes = Encoding.UTF8.GetBytes(password);
            byte[] hashBytes = sha.ComputeHash(bytes);
            return Convert.ToBase64String(hashBytes);
        }

        public static bool Verify(string password, string hash)
        {
            return Hash(password) == hash;
        }
    }
}
