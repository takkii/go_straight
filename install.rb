# frozen_string_literal: true
#!/usr/bin/ruby

require 'open3'

# Installer runner.
class InstallerRunner
  # default encoding utf-8, change encode here.
  def self.encoding_style
    Encoding.default_internal = 'UTF-8'
    Encoding.default_external = 'UTF-8'
  end

  def self.run
    encoding_style
    if Dir.exist?(File.expand_path('~/config'))
      stdout_rb, _stderr_rb, _status_rb = Open3.capture3("ruby ./uninstaller.rb")
      stdout_rb
    else
      stdout_rb, _stderr_rb, _status_rb = Open3.capture3("git clone git@github.com:takkii/config.git && mv config ~/")
      stdout_rb
    end
  end
end

InstallerRunner.run