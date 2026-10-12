using System;
using System.IO;
using System.Diagnostics;

namespace ANAIRelight
{
    internal class Program
    {
        static int Main(string[] args)
        {
            Console.WriteLine("AN AI Relight Engine");
            Console.WriteLine("Version 6.0 Local AI");


            string basePath =
                AppDomain.CurrentDomain.BaseDirectory;


            string runtime =
                Path.Combine(basePath, "runtime");


            string models =
                Path.Combine(basePath, "models");


            if (!Directory.Exists(runtime))
            {
                Console.WriteLine("Runtime missing");
                return 1;
            }


            if (!Directory.Exists(models))
            {
                Console.WriteLine("Models missing");
                return 2;
            }


            Console.WriteLine("Environment OK");


            if(args.Length > 0)
            {
                StartWorker(runtime, args[0]);
            }


            return 0;
        }


        static void StartWorker(string runtime, string input)
        {

            string worker =
                Path.Combine(runtime, "worker.py");


            if(!File.Exists(worker))
            {
                Console.WriteLine("Worker missing");
                return;
            }


            Process.Start(
                "python",
                $"\"{worker}\" \"{input}\""
            );

        }
    }
}
