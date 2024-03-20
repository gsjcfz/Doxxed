using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Hosting;
using Python.Runtime;
using Microsoft.AspNetCore.Authorization; // Import Python.Runtime namespace

namespace Doxxed.Pages
{
    [Authorize]
    public class IndexModel : PageModel
    {
        private readonly IWebHostEnvironment _env;

        public IndexModel(IWebHostEnvironment env)
        {
            _env = env;
        }

        [BindProperty]
        public string Username { get; set; }

        public string ScriptOutput { get; set; }

        public void OnPost()
        {
            if (!ModelState.IsValid)
            {
                return;
            }

            Runtime.PythonDLL = @"C:\Users\16363\AppData\Local\Programs\Python\Python312\python312.dll";
            PythonEngine.Initialize();

            using (Py.GIL()) // Acquire the GIL (Global Interpreter Lock)
            {
                try
                {
                    // Construct the path to the script directory
                    string scriptPath = System.IO.Path.Combine(_env.ContentRootPath, "");
                    // Add the script directory to Python's search path
                    dynamic sys = Py.Import("sys");
                    sys.path.append(scriptPath);

                    // Now import your script and run the function
                    dynamic script = Py.Import("script");
                    ScriptOutput = script.run(Username).ToString();
                }
                catch (PythonException ex)
                {
                    ScriptOutput = $"Failed to run Python script: {ex.Message}";
                }
            }

            PythonEngine.Shutdown();
        }
    }
}