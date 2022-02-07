# frozen_string_literal: true
#!/usr/bin/ruby

require 'open3'

# Installer runner.
class PyLibInstallerRunner
  # default encoding utf-8, change encode here.
  def self.encoding_style
    Encoding.default_internal = 'UTF-8'
    Encoding.default_external = 'UTF-8'
  end

  def self.run
    encoding_style
    stdout_rb, _stderr_rb, _status_rb = Open3.capture3("pip3 install -r requirements.txt")
    puts stdout_rb
  end
end

PyLibInstallerRunner.run