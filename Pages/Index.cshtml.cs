using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Hosting;
using Python.Runtime;
using Microsoft.AspNetCore.Authorization; // Import Python.Runtime namespace
using Microsoft.Extensions.Logging;
namespace Doxxed.Pages
{
    [Authorize]
    public class IndexModel : PageModel
    {
        private readonly ILogger<IndexModel> _logger; // Declare a logger variable
        private readonly IWebHostEnvironment _env;

        // Inject ILogger and IWebHostEnvironment via constructor
        public IndexModel(ILogger<IndexModel> logger, IWebHostEnvironment env)
        {
            _logger = logger; // Initialize the logger
            _env = env;
        }

        [BindProperty]
        public string Username { get; set; }

        // will bind the rest 
        [BindProperty]
        public string Email { get; set; }

       
        public string PhoneNumber { get; set; }

        [BindProperty]
        public string IpAddress { get; set; }

        
        public string FirstName { get; set; }

       
        public string LastName { get; set; }

        public string ScriptOutput { get; set; }
        public string HtmlContent { get; set; } // To store the HTML content
        


        public void OnPost()
        {
            _logger.LogInformation("Post action started.");


            try
            {
                _logger.LogInformation("Initializing Python engine.");
                Runtime.PythonDLL = @"C:\Users\16363\AppData\Local\Programs\Python\Python312\python312.dll";
                PythonEngine.Initialize();

                using (Py.GIL())
                {
                    _logger.LogInformation("Python GIL acquired.");
                    string scriptPath = System.IO.Path.Combine(_env.ContentRootPath, "");
                    _logger.LogInformation($"Script path: {scriptPath}");

                    dynamic sys = Py.Import("sys");
                    sys.path.append(scriptPath);
                    _logger.LogInformation("Script path appended to Python sys.path.");

                    dynamic script = Py.Import("script");
                    _logger.LogInformation("Python script imported successfully.");

                    dynamic result = script.osint_gather_and_send(username: Username, ip_addr: IpAddress);
                    ScriptOutput = result.ToString();
                    
                    _logger.LogInformation("Python script executed.");
                }
            }
            catch (PythonException ex)
            {
                _logger.LogError($"Python error: {ex.Message}");
                ScriptOutput = $"Failed to run Python script: {ex.Message}";
            }
            catch (Exception ex)
            {
                _logger.LogError($"General error: {ex.ToString()}");
                ScriptOutput = $"An unexpected error occurred: {ex.Message}";
            }
            finally
            {
                PythonEngine.Shutdown();
                _logger.LogInformation("Python engine shutdown.");
            }
            // Assuming username is not null and the HTML file is named after the username
            var filePath = Path.Combine(_env.ContentRootPath, @"Data\", $"{Username}.html");
            _logger.LogInformation(filePath);
            if (System.IO.File.Exists(filePath))
            {
                HtmlContent = System.IO.File.ReadAllText(filePath);
            }
            else
            {
                HtmlContent = "The requested file does not exist.";
            }
        }  

    }
}