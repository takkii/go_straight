# frozen_string_literal: true
#!/usr/bin/ruby

require 'open3'

# Installer runner.
class UnInstallerRunner
  # default encoding utf-8, change encode here.
  def self.encoding_style
    Encoding.default_internal = 'UTF-8'
    Encoding.default_external = 'UTF-8'
  end

  def self.run
    encoding_style
    stdout_rb, _stderr_rb, _status_rb = Open3.capture3("rm ~/config")
    stdout_rb
  end
end

UnInstallerRunner.run